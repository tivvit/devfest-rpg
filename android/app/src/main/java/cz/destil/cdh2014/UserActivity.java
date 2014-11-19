package cz.destil.cdh2014;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import java.util.List;

import butterknife.ButterKnife;
import butterknife.InjectView;
import cz.destil.cdh2014.api.Api;
import cz.destil.cdh2014.api.model.Quest;
import cz.destil.cdh2014.api.model.UserStats;
import cz.destil.cdh2014.data.Preferences;
import cz.destil.cdh2014.util.Toas;
import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;


public class UserActivity extends Activity {

    String userId;

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
                addToFaction.setEnabled(userStats.allowedToFaction.equals("1"));
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
            if (name.length() > 50) {
                name = name.substring(0, 50);
            }
            text += name + " | " + quest.points + " bodů | " + quest.faction;
            if (i != quests.size() - 1) {
                text += "\n";
            }
            i++;
        }
        textView.setText(text);
    }
}
