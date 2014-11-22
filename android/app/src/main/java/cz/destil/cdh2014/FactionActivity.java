package cz.destil.cdh2014;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import cz.destil.cdh2014.data.Preferences;


public class FactionActivity extends Activity {

    public static final String[] FACTIONS = new String[] { "Exodité", "Metalidé", "Vitalisté" };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_faction);
        ListView list = (ListView) findViewById(R.id.list);
        list.setAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, FACTIONS));
        list.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                Preferences.setFaction(position + 1);
                startActivity(new Intent(FactionActivity.this, MainActivity.class));
                finish();
            }
        });
    }

}
