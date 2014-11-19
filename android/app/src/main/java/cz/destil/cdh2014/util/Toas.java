package cz.destil.cdh2014.util;

import android.widget.Toast;

import cz.destil.cdh2014.App;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class Toas {
    public static void t(String text) {
        Toast.makeText(App.get(), text, Toast.LENGTH_LONG).show();
    }
}
