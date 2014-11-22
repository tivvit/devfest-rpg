package cz.destil.cdh2014.api.model;

/**
 * TODO
 *
 * @author David Vávra (david@vavra.me)
 */
public class Quest {
    public String points;
    public InnerQuest quest;

    public static class InnerQuest {
        public String points;
        public String name;
        public String faction;
    }
}
