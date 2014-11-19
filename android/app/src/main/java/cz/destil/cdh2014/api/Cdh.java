package cz.destil.cdh2014.api;

import cz.destil.cdh2014.api.model.Users;
import retrofit.Callback;
import retrofit.http.GET;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public interface Cdh {
    @GET("/user")
    public void listUsers(Callback<Users> cb);
}
