import React from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import styles from '../Styles/Styles.js';
import { items } from '../Data/Items.js';

export default function BrowseScreen({ navigation }) {
  const renderItem = ({ item }) => (
    <TouchableOpacity style={styles.listItem} onPress={() => navigation.navigate('ItemDetail', { item })}>
      <Text style={styles.listItemTitle}>{item.title}</Text>
      <Text style={styles.listItemSub}>{item.location} • Udlejer: {item.owner}</Text>
      <Text style={styles.price}>{item.pricePerDay} kr/døgn</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Ting i nærheden</Text>
      <FlatList
        data={items}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
}