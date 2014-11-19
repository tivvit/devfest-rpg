package cz.destil.cdh2014.api;

import retrofit.RestAdapter;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class Api {
    public static Cdh get() {
        RestAdapter restAdapter = new RestAdapter.Builder().setLogLevel(RestAdapter.LogLevel.BASIC)
                .setEndpoint("https://practical-well-728.appspot.com/_ah/api/devfest_cdh_api/v1")
                .build();
        return restAdapter.create(Cdh.class);
    }
}
