package cz.destil.cdh2014;

import android.app.Application;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class App extends Application {

    private static App instance = null;

    @Override
    public void onCreate() {
        super.onCreate();
        instance = this;
    }

    public static App get() {
        return instance;
    }

}
