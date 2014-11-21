package cz.destil.cdh2014.api;

import cz.destil.cdh2014.api.model.FactionHiring;
import cz.destil.cdh2014.api.model.UserStats;
import cz.destil.cdh2014.api.model.Users;
import retrofit.Callback;
import retrofit.http.GET;
import retrofit.http.POST;
import retrofit.http.Path;
import retrofit.http.Query;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public interface Cdh {
    @GET("/user")
    public void listUsers(Callback<Users> cb);

    @GET("/factionHiring/{faction}")
    public void factionHiring(@Path("faction") int factionId, Callback<FactionHiring> cb);

    @GET("/userStats/{userId}")
    public void userStats(@Path("userId") String userId, @Query("faction_id") int factionId, Callback<UserStats> cb);

    @POST("/questSolved/{userId}")
    public void questSolved(@Path("userId") String userId, @Query("quest_id") int questId, Callback<Object> cb);

    @POST("/setFraction/{userId}")
    public void setFaction(@Path("userId") String userId, @Query("faction_id") int factionId, Callback<Object> cb);

    @POST("/givePoints/{userId}")
    public void givePoints(@Path("userId") String userId, @Query("points") int points, Callback<Object> cb);
}
