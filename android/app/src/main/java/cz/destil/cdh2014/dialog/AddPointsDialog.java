package cz.destil.cdh2014.dialog;

import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.View;

import cz.destil.cdh2014.R;

import eu.inmite.android.lib.dialogs.BaseDialogFragment;
import eu.inmite.android.lib.dialogs.SimpleDialogFragment;

public class AddPointsDialog extends SimpleDialogFragment {

    public static String TAG = "jayne";

    public static void show(FragmentActivity activity) {
        new AddPointsDialog().show(activity.getSupportFragmentManager(), TAG);
    }

    @Override
    public BaseDialogFragment.Builder build(BaseDialogFragment.Builder builder) {
        builder.setTitle("Přidat ad-hoc body");
        builder.setView(LayoutInflater.from(getActivity()).inflate(R.layout.part_edit, null));
        builder.setPositiveButton("Přidat", new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO
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
