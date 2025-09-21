import React from 'react';
import { View, Text, TouchableOpacity, Alert } from 'react-native';
import styles from '../Styles/Styles.js';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Velkommen til LejTing 👋</Text>
      <Text>Lej ting du sjældent bruger – hurtigt og billigt.</Text>

      {/* Knap 1: Naviger til liste (opfylder kravet om navigation) */}
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Browse')}>
        <Text style={styles.buttonText}>Se ting i nærheden</Text>
      </TouchableOpacity>

      {/* Knap 2: Simpel funktion (Alert) */}
      <TouchableOpacity style={styles.button} onPress={() => Alert.alert('Tip', 'Brug listen til at vælge en ting og send en forespørgsel!')}>
        <Text style={styles.buttonText}>Hvordan virker det?</Text>
      </TouchableOpacity>
    </View>
  );
}