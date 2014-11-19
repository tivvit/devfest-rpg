import 'dart:html';
import 'dart:convert';

var baseUrl = "https://practical-well-728.appspot.com/_ah/api/devfest_cdh_api/v1/";

void main() {
  querySelector("#searchForm")
          ..onSubmit.listen(submitForm);
  
  window.onHashChange.listen(hashChange);
}

void submitForm(Event e) {
  e.preventDefault();
  InputElement i = querySelector("#searchForm input[name=query]");
  loadPeople(i.value);
}

void hashChange(HashChangeEvent e) {
  String id = window.location.hash;
  id = id.substring(1);
  print("------");
  print(id);
  print("------");
  querySelector("#people").style.display = 'none';
  querySelector("#person").style.display = 'show';
  var userApi = baseUrl + "user/" + id;
  HttpRequest.getString(userApi).then(onPersonLoaded);
  var questsApi = baseUrl + "user/" + id;
  HttpRequest.getString(questsApi).then(onPersonLoaded);
}

void onPersonLoaded(String responseText) {
  Map userJson = JSON.decode(responseText);
  print("=========");
  print(userJson);
  
  //Element person = querySelector("#person");
  querySelector("#person .name").text = userJson["name"]; 
  querySelector("#person .email").text = userJson["email"]; 
  querySelector("#person .faction").text = userJson["faction"]; 
  //person.append(row);
  
  /*
  for (var player in userJson["user"]) {
      //print(player);
      Element row = new Element.tag('tr')
          ..id = player["id"]
          ..append(new Element.tag('td')..text = player["name"])
          ..append(new Element.tag('td')..text = player["faction"])
          ..onClick.listen(loadPerson);
      

      querySelector("#people").append(row);
    }
     */
}

void loadPeople(String query) {
  querySelector("#people").style.display = 'block';
  querySelector("#person").style.display = 'hide';
  var url = baseUrl + "userSearch/" + query;
  var request = HttpRequest.getString(url).then(onPeopleLoaded);
}

void loadPerson(MouseEvent event) {
  //print(event.currentTarget.id);
  Element e = event.currentTarget;
  window.location.hash = e.id;
  
}

void onPeopleLoaded(String responseText) {
  Map userJson = JSON.decode(responseText);
  print(userJson);
  
  for (var player in userJson["user"]) {
      //print(player);
      Element row = new Element.tag('tr')
          ..id = player["id"]
          ..append(new Element.tag('td')..text = player["name"])
          ..append(new Element.tag('td')..text = player["faction"])
          ..onClick.listen(loadPerson);
      

      querySelector("#people").append(row);
    }
}