import React from 'react';
import { View, Text, TouchableOpacity, Alert } from 'react-native';
import styles from '../Styles/Styles.js';
// Forsiden der skal introducere ideen og har en knap til at gå videre til Browse siden
export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Velkommen til LejTing 👋</Text>
      <Text>Lej ting du sjældent bruger – hurtigt og billigt.</Text>

      {// Knap 1: Naviger til liste //}
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Browse')}>
        <Text style={styles.buttonText}>Se ting i nærheden</Text>
      </TouchableOpacity>

      {// Knap der hjælper nye brugere: viser en kort forklaring på hvordan appen bruges //}
      <TouchableOpacity style={styles.button} onPress={() => Alert.alert('Tip', 'Brug listen til at vælge en ting og send en forespørgsel!')}>
        <Text style={styles.buttonText}>Hvordan virker det?</Text>
      </TouchableOpacity>
    </View>
  );
}
