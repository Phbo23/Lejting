import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import HomeScreen from './Screens/HomeScreen';
import BrowseScreen from './Screens/BrowseScreen';
import ItemDetailScreen from './Screens/ItemDetailScreen';
// Der bruges stack navigation til at kunne skifte mellem forskellige sider i appen.
const Stack = createNativeStackNavigator();

// NavigationContainer holder hele navigationen i live
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'LejTing' }} />
        <Stack.Screen name="Browse" component={BrowseScreen} options={{ title: 'Ting i nærheden' }} />
        <Stack.Screen name="ItemDetail" component={ItemDetailScreen} options={{ title: 'Detaljer' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
