import React from 'react';
import { View, Text, TouchableOpacity, Alert } from 'react-native';
import styles from '../Styles/Styles.js';
// Viser detaljer om en ting (fx ejer, lokation, pris)
export default function ItemDetailScreen({ route }) {
  const { item } = route.params;

  const requestToRent = () => {
    // Simulerer en forespørgsel om at leje
    Alert.alert('Forespørgsel sendt', `Du har forespurgt på at leje "${item.title}". Udlejer kontakter dig.`);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{item.title}</Text>
      <Text>Ejer/udlejer: {item.owner}</Text>
      <Text>Lokation: {item.location}</Text>
      <Text style={styles.price}>{item.pricePerDay} kr/døgn</Text>

      <TouchableOpacity style={styles.button} onPress={requestToRent}>
        <Text style={styles.buttonText}>Anmod om at leje</Text>
      </TouchableOpacity>
    </View>
  );
}
