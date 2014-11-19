package cz.destil.cdh2014.api.model;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class User {
    public String name;
    public String email;
    public String id;

    @Override
    public String toString() {
        return name+" ("+email+")";
    }
}
