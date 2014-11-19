package cz.destil.cdh2014;

import android.app.Application;

import com.squareup.otto.Bus;

import java.util.List;

import cz.destil.cdh2014.api.Api;
import cz.destil.cdh2014.api.model.User;
import cz.destil.cdh2014.api.model.Users;
import cz.destil.cdh2014.event.UsersDownloadedEvent;
import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class App extends Application {

    private static App instance = null;
    private static Bus bus = null;
    public static List<User> users = null;

    @Override
    public void onCreate() {
        super.onCreate();
        instance = this;
        bus = new Bus();
    }

    public static App get() {
        return instance;
    }

    public static Bus bus() {
        return bus;
    }

    public static void downloadUsersIfNeccessary() {
        if (users == null) {
            Api.get().listUsers(new Callback<Users>() {
                @Override
                public void success(Users user, Response response) {
                    users = user.user;
                    Toas.t("Uzivatelé staženi ze serveru");
                    bus.post(new UsersDownloadedEvent());
                }

                @Override
                public void failure(RetrofitError error) {
                    Toas.t("Stahování uživatelů selhalo: " + error.toString());
                }
            });
        }
    }

}
