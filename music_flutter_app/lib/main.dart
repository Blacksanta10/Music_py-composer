import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// Main function that tells flutter to run app object
void main() {
  runApp(MyApp());
}

// The MyApp class has defines widgets used in app
// this class sets up the whole app
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyAppState(),
      child: MaterialApp(
        title: 'Namer App',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange),
        ),
        home: MyHomePage(),
      ),
    );
  }
}

// defines the app's state or the data needed for the app to run
class MyAppState extends ChangeNotifier {
  var current = WordPair.random();

  void getNext() {
    current = WordPair.random(); // reassigns current with new word pair
    notifyListeners(); // method of ChangeNotifier, ensures that anyone watching MyAppState is notified
  }

  var favorites = <WordPair>[];

  void toggleFavorite() {
    if (favorites.contains(current)) {
      favorites.remove(current);
    } else {
      favorites.add(current);
    }
    notifyListeners();
  }
}


// Each build method returns a widget (Scaffold, Text, Column)
class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() =>
  _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var selectedIndex = 0;  //keep track of this variable

  @override
  Widget build(BuildContext context) {
    Widget page;
    switch (selectedIndex) {
      case 0:
        page = GeneratorPage();
        break;
      case 1:
        page = Placeholder();
        break;
      default:
        throw UnimplementedError('no widget for $selectedIndex');
    }
    return LayoutBuilder(builder: (context, constraints) {
        return Scaffold(
          body: Row(              
              children: [
                SafeArea(
                  child: NavigationRail(
                    extended: constraints.maxWidth >= 600, //adds reponsive features
                    
                    destinations: [
        
                      NavigationRailDestination(
                        icon: Icon(Icons.home),
                        label: Text('Home'),
                        ),
        
                        NavigationRailDestination(
                          icon: Icon(Icons.favorite),
                          label: Text('Favorites'),
                        ),
                      ], //destinations array
                    selectedIndex: selectedIndex,
                    onDestinationSelected: (value) {
        
                      setState(() {
                        selectedIndex = value;  //the value changes when destination is selected. The value is assigned to the new value.
                      });
        
                    },
                  ),
                ),
                
                //expanded widgets are greedy
                Expanded(
                  child: Container(
                    color: Theme.of(context).colorScheme.primaryContainer,
                    child: page,
                  ),
                ),
              ], 
          ),
        );
      }
    );
  }
}

class GeneratorPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var appState = context.watch<MyAppState>();
    var pair = appState.current;  // widget for word pair

    IconData icon;
    if (appState.favorites.contains(pair)) {
      icon = Icons.favorite;
    } else {
      icon = Icons.favorite_border;
    }

    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          BigCard(pair: pair),
          SizedBox(height: 10),
          Row(
            mainAxisSize: MainAxisSize.min,

            children: [
              ElevatedButton.icon(
                onPressed: () {
                  appState.toggleFavorite();
                },
                icon: Icon(icon),
                label: Text('Like'),
              ),

              SizedBox(width: 10),

              ElevatedButton(
                onPressed: () {
                  appState.getNext();
                },
                child: Text('Next'),
              ),

            ],

          )
        ],
      ),
    );

  }
}

class BigCard extends StatelessWidget {
  const BigCard({
    super.key,
    required this.pair,
  });

  final WordPair pair;

  @override
  // build method for BigCard
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final style = theme.textTheme.displayMedium!.copyWith(
      color: theme.colorScheme.onPrimary,
    );

    return Card(
      color: theme.colorScheme.primary, // card's color from app's color scheme
      child: Padding(
        padding: const EdgeInsets.all(20),

        child: Text(
          pair.asLowerCase,
          style: style,
          semanticsLabel: "${pair.first} ${pair.second}",
        ),
      ),
    );
  }
}