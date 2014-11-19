package cz.destil.cdh2014;

import android.widget.Toast;

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
