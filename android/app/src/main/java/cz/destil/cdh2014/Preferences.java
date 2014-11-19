package cz.destil.cdh2014;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class Preferences {
    public static int getFaction() {
        return get().getInt("FACTION", -1);
    }

    public static void setFaction(int factionId) {
        get().edit().putInt("FACTION", factionId).commit();
    }

    private static SharedPreferences get() {
        return PreferenceManager.getDefaultSharedPreferences(App.get());
    }
}
