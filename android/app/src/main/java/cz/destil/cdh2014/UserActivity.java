package cz.destil.cdh2014;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.widget.Button;
import android.widget.TextView;

import java.util.List;

import butterknife.ButterKnife;
import butterknife.InjectView;
import butterknife.OnClick;
import cz.destil.cdh2014.api.Api;
import cz.destil.cdh2014.api.model.Quest;
import cz.destil.cdh2014.api.model.UserStats;
import cz.destil.cdh2014.data.Preferences;
import cz.destil.cdh2014.dialog.AddPointsDialog;
import cz.destil.cdh2014.util.Toas;
import eu.inmite.android.lib.dialogs.ISimpleDialogListener;
import eu.inmite.android.lib.dialogs.SimpleDialogFragment;
import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;


public class UserActivity extends FragmentActivity implements ISimpleDialogListener {

    static final int FACTION_DIALOG = 42;

    String userId;
    boolean previousPossibleToJoin = true;

    @InjectView(R.id.nameEmail)
    TextView nameEmail;
    @InjectView(R.id.factionPoints)
    TextView factionPoints;
    @InjectView(R.id.addToFaction)
    Button addToFaction;
    @InjectView(R.id.todo)
    TextView todo;
    @InjectView(R.id.completed)
    TextView completed;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user);
        ButterKnife.inject(this);
        userId = getIntent().getStringExtra("USER_ID");
        download();
    }

    private void download() {
        Api.get().userStats(userId, Preferences.getFaction(), new Callback<UserStats>() {
            @Override
            public void success(UserStats userStats, Response response) {
                nameEmail.setText(userStats.user.name + " (" + userStats.user.email + ")");
                factionPoints.setText(userStats.user.faction + " - " + userStats.pointsSum);
                setQuests(todo, userStats.todo);
                setQuests(completed, userStats.quests);
                boolean possibleToJoin = userStats.allowedToFaction.equals("1");
                if (!previousPossibleToJoin && possibleToJoin) {
                    SimpleDialogFragment.createBuilder(UserActivity.this, getSupportFragmentManager()).setMessage("Tototo hráče je nyní možné " +
                            "přijmout do frakce!").setNegativeButtonText("Zavřít").show();
                }
                addToFaction.setEnabled(possibleToJoin);
            }

            @Override
            public void failure(RetrofitError error) {
                Toas.t("Načítání uživatele selhalo: " + error.toString());
            }
        });
    }

    private void setQuests(TextView textView, List<Quest> quests) {
        String text = "";
        int i = 0;
        for (Quest quest : quests) {
            String name = quest.name;
            final int MAX_NAME_LENGTH = 21;
            if (name.length() > MAX_NAME_LENGTH) {
                name = name.substring(0, MAX_NAME_LENGTH);
            }
            text += name + " | " + quest.points + " bodů | " + quest.faction;
            if (i != quests.size() - 1) {
                text += "\n";
            }
            i++;
        }
        textView.setText(text);
    }

    @OnClick(R.id.addToFaction)
    public void onFactionClick() {
        SimpleDialogFragment.createBuilder(this, getSupportFragmentManager()).setTitle("Opravdu přijmout do frakce?")
                .setPositiveButtonText("Ano").setNegativeButtonText("Ne").setRequestCode(FACTION_DIALOG).show();
    }

    @OnClick(R.id.completeQuest)
    public void onCompleteQuest() {
        try {
            Intent intent = new Intent("com.google.zxing.client.android.SCAN");
            intent.putExtra("SCAN_MODE", "QR_CODE_MODE"); // "PRODUCT_MODE for bar codes
            startActivityForResult(intent, 0);
        } catch (Exception e) {
            Uri marketUri = Uri.parse("https://play.google.com/store/apps/details?id=eu.inmite.prj.vf.reader");
            Intent marketIntent = new Intent(Intent.ACTION_VIEW, marketUri);
            startActivity(marketIntent);
        }
    }

    @OnClick(R.id.adHoc)
    public void onAdHoc() {
        AddPointsDialog.show(this);
    }

    @Override
    public void onPositiveButtonClicked(int requestCode) {
        if (requestCode == FACTION_DIALOG) {
            Api.get().setFaction(userId, Preferences.getFaction(), new Callback<Object>() {
                @Override
                public void success(Object o, Response response) {
                    Toas.t("Hráč už je navždy váš!");
                    download();
                }

                @Override
                public void failure(RetrofitError error) {
                    Toas.t("Nepodařilo se uložit přijmutí hráče do frakce. Možná už nenabíráte.");
                }
            });
        } else if (requestCode == AddPointsDialog.ADD_POINTS_DIALOG) {
            Api.get().givePoints(userId, AddPointsDialog.numberOfPoints, new Callback<Object>() {
                @Override
                public void success(Object o, Response response) {
                    Toas.t(AddPointsDialog.numberOfPoints+" bodů připsáno hráči.");
                    download();
                }

                @Override
                public void failure(RetrofitError error) {
                    Toas.t("Nepodařilo se uložit body na server.");
                }
            });
        }
    }

    @Override
    public void onNegativeButtonClicked(int i) {

    }

    @Override
    public void onNeutralButtonClicked(int i) {

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 0) {
            if (resultCode == RESULT_OK) {
                String contents = data.getStringExtra("SCAN_RESULT");
                int questId = -1;
                try {
                    questId = Integer.parseInt(contents.split("#X")[1]);
                } catch (Exception e) {
                    Toas.t("Nascanován špatný QR kód");
                }
                if (questId != -1) {
                    Api.get().questSolved(userId, questId, new Callback<Object>() {
                        @Override
                        public void success(Object o, Response response) {
                            Toas.t("Quest úspěšně splněn");
                            download();
                        }

                        @Override
                        public void failure(RetrofitError error) {
                            Toas.t("Zapsání questu SELHALO!");
                        }
                    });
                }

            }
        }
    }

}
