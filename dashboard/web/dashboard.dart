import 'dart:html';
import 'dart:convert';
import 'package:chart/chart.dart';

var baseUrl = "https://practical-well-728.appspot.com/_ah/api/devfest_cdh_api/v1/";

void loadStats() {
  var url = baseUrl + "stats";
  var request = HttpRequest.getString(url).then(onStatsLoaded);
}

void loadLeaderboard() {
  var url = baseUrl + "leaderboard/20";
  var request = HttpRequest.getString(url).then(onLeaderboardLoaded);
}

void onStatsLoaded(String responseText) {
  Map statsJson = JSON.decode(responseText);
  print(statsJson["stats"]);
  print(statsJson["users"]);

  var users = statsJson["users"];
  var stats = statsJson["stats"];

  var statsData = [int.parse(stats[0]["points"]), int.parse(stats[1]["points"]), int.parse(stats[2]["points"])];
  var userData = [int.parse(users[0]["users"]), int.parse(users[1]["users"]), int.parse(users[2]["users"])];

  var usersMax = 0;
  for (var users in userData) {
    if (users > usersMax) usersMax = users;
  }

  var statsMax = 0;
  for (var points in statsData) {
    if (points > statsMax) statsMax = points;
  }

  Bar statsBar = new Bar({
    //'labels': ["Exodité", "Metalidé", "Vitalisté"],
    'labels': ["", "", ""],
    'datasets': [{
        'fillColor': "rgba(75,164,227,0.5)",
        'data': statsData
      }]
  }, {
    'titleText': 'Výzkumné body',
    'scaleMinValue': 0.0,
    'barShowStroke': false,
    'scaleOverride': true,
    'scaleMaxValue': statsMax,
  });

  Bar usersBar = new Bar({
    'labels': ["1", "2", "3"],
    'datasets': [{
        'fillColor': "rgba(29,168,66,0.5)",
        'data': userData
      }]
  }, {
    'titleText': 'Users per faction',
    'scaleMinValue': 0.0,
    'barShowStroke': false,
    'scaleOverride': true,
    'scaleMaxValue': usersMax,
  });

  var statsElem = querySelector("#stats")..style.height = '400px';
  statsBar.show(statsElem);

  var usersElem = querySelector("#users")..style.height = '400px';
  usersBar.show(usersElem);

}

void onLeaderboardLoaded(String responseText) {
  Map stats = JSON.decode(responseText);
  print(stats["leaderboard1"]);

  var leaderboard1 = querySelector("#leaderboard1 tbody");
  var leaderboard2 = querySelector("#leaderboard2 tbody");

  int cntr = 0;
  for (var player in stats["leaderboard"]) {
    //print(player);
    Element row = new Element.tag('tr')
        ..append(new Element.tag('td')..text = player["user"]["name"])
        ..append(new Element.tag('td')..text = player["points"])
        ..append(new Element.tag('td')..text = player["user"]["faction"]);

    if(cntr < 10)
      leaderboard1.append(row);
    else
      leaderboard2.append(row);
    
    cntr++;
  }
}

main() {
  loadStats();
  loadLeaderboard();
}
