package cz.destil.cdh2014.dialog;

import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;

import cz.destil.cdh2014.R;
import cz.destil.cdh2014.util.Toas;
import eu.inmite.android.lib.dialogs.BaseDialogFragment;
import eu.inmite.android.lib.dialogs.ISimpleDialogListener;
import eu.inmite.android.lib.dialogs.SimpleDialogFragment;

public class AddPointsDialog extends SimpleDialogFragment {

    public static String TAG = "jayne";
    public static int ADD_POINTS_DIALOG = 41;
    private static FragmentActivity activity;
    public static int numberOfPoints = 0;

    public static void show(FragmentActivity activity) {
        AddPointsDialog.activity = activity;
        new AddPointsDialog().show(activity.getSupportFragmentManager(), TAG);
    }

    @Override
    public BaseDialogFragment.Builder build(BaseDialogFragment.Builder builder) {
        builder.setTitle("Přidat ad-hoc body");
        final View view = LayoutInflater.from(getActivity()).inflate(R.layout.part_edit, null);
        builder.setView(view);
        builder.setPositiveButton("Přidat", new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (activity instanceof ISimpleDialogListener) {
                    try {
                        numberOfPoints = Integer.parseInt(((EditText) view.findViewById(R.id.points)).getText().toString());
                        ((ISimpleDialogListener) activity).onPositiveButtonClicked(ADD_POINTS_DIALOG);
                    } catch (Exception e) {
                        Toas.t("Zadali jste nějakou kravinu");
                        e.printStackTrace();
                    }
                }
                dismiss();
            }
        });
        builder.setNegativeButton("Zrušit", new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dismiss();
            }
        });
        return builder;
    }
}
