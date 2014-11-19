package cz.destil.cdh2014;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (Preferences.getFaction() == -1) {
            startActivity(new Intent(this, FactionActivity.class));
            finish();
        } else {
            setContentView(R.layout.activity_main);
        }
    }
}
