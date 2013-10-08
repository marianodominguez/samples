import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.client.HazelcastClient;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IMap;

clientConfig = new ClientConfig()
clientConfig.addAddress "127.0.0.1:5701"
client = HazelcastClient.newHazelcastClient clientConfig
map = client.getMap "customers"
println "Map Size:" + map.size()

if (map.size() == 0) {
   map.put(1, "Mariano")
   map.put(2, "Sofia")
   map.put(3, "Ligia")
} else {
  println map
}

client.shutdown()