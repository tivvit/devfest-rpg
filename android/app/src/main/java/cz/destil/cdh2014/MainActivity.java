package cz.destil.cdh2014;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.TextView;

import com.squareup.otto.Subscribe;

import butterknife.ButterKnife;
import butterknife.InjectView;
import cz.destil.cdh2014.api.Api;
import cz.destil.cdh2014.api.model.FactionHiring;
import cz.destil.cdh2014.api.model.FactionMinPoints;
import cz.destil.cdh2014.api.model.User;
import cz.destil.cdh2014.data.Preferences;
import cz.destil.cdh2014.event.UsersDownloadedEvent;
import cz.destil.cdh2014.util.Toas;
import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;


public class MainActivity extends Activity {

    @InjectView(R.id.autocomplete)
    AutoCompleteTextView autoComplete;
    @InjectView(R.id.faction)
    TextView faction;
    @InjectView(R.id.factionMin)
    TextView factionMin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        App.bus().register(this);
        if (Preferences.getFaction() == -1) {
            startActivity(new Intent(this, FactionActivity.class));
            finish();
        } else {
            setContentView(R.layout.activity_main);
            ButterKnife.inject(this);
            setupUsers();
            faction.setText(FactionActivity.FACTIONS[Preferences.getFaction() - 1]);
        }
        App.downloadUsersIfNeccessary();
    }

    @Override
    protected void onStart() {
        super.onStart();
        if (Preferences.getFaction() != -1) {
            autoComplete.setText("");
            Api.get().factionHiring(Preferences.getFaction(), new Callback<FactionHiring>() {
                @Override
                public void success(FactionHiring factionHiring, Response response) {
                    String factionText = FactionActivity.FACTIONS[Preferences.getFaction() - 1];
                    if (factionHiring.hiring.equals("1")) {
                        factionText+=" - frakce otevřená novým členům";
                    } else {
                        factionText+=" - frakce je UZAVŘENÁ pro nové členy";
                    }
                    faction.setText(factionText);
                }

                @Override
                public void failure(RetrofitError error) {
                    Toas.t("Nepodařilo se zjistit, jestli frakce nabírá nebo ne: " + error.toString());
                }
            });
            Api.get().factionMinPoints(new Callback<FactionMinPoints>() {
                @Override
                public void success(FactionMinPoints factionMinPoints, Response response) {
                    factionMin.setText(factionMinPoints.min);
                }

                @Override
                public void failure(RetrofitError error) {
                    Toas.t("Nepodařilo se stáhnout min počet bodů do frakce");
                }
            });
        }
    }

    @Override
    protected void onDestroy() {
        App.bus().unregister(this);
        super.onDestroy();
    }

    private void setupUsers() {
        autoComplete.setAdapter(new ArrayAdapter<User>(this, android.R.layout.simple_dropdown_item_1line, App.users));
        autoComplete.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                Intent i = new Intent(MainActivity.this, UserActivity.class);
                i.putExtra("USER_ID", App.users.get(position).id);
                startActivity(i);
            }
        });
    }

    @Subscribe
    public void onUsersDownloaded(UsersDownloadedEvent event) {
        setupUsers();
    }
}
