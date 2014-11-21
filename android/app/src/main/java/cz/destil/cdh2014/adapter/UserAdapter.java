package cz.destil.cdh2014.adapter;

import java.util.List;

import android.content.Context;
import android.widget.ArrayAdapter;

import cz.destil.cdh2014.api.model.User;

/**
 * Created by vavra on 21/11/14.
 */
public class UserAdapter extends ArrayAdapter<User> {
    public UserAdapter(Context context, int resource, List<User> objects) {
        super(context, resource, objects);
    }

    @Override
    public long getItemId(int position) {
        return Long.parseLong(getItem(position).id);
    }
}
