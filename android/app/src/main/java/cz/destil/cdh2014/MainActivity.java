package cz.destil.cdh2014;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.TextView;

import com.squareup.otto.Subscribe;

import butterknife.ButterKnife;
import butterknife.InjectView;
import cz.destil.cdh2014.api.model.User;
import cz.destil.cdh2014.event.UsersDownloadedEvent;


public class MainActivity extends Activity {

    @InjectView(R.id.autocomplete)
    AutoCompleteTextView autoComplete;
    @InjectView(R.id.faction)
    TextView faction;

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
            setup();
        }
        App.downloadUsersIfNeccessary();
    }

    @Override
    protected void onDestroy() {
        App.bus().unregister(this);
        super.onDestroy();
    }

    private void setup() {
        autoComplete.setAdapter(new ArrayAdapter<User>(this, android.R.layout.simple_dropdown_item_1line, App.users));
        faction.setText(FactionActivity.FACTIONS[Preferences.getFaction() - 1]);
    }

    @Subscribe
    public void onUsersDownloaded(UsersDownloadedEvent event) {
        setup();
    }
}
