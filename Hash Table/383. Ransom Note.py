class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

       HashMap<Character, Integer> map = new HashMap<>();
       for (char c : magazine.toCharArray()) {
            if (map.containsKey(c)) {
                int count = map.get(c);
                map.put(c, count + 1);
            } else {
                map.put(c, 1);
            }
       }
    

       for (char c : ransomNote.toCharArray()) {
           if (!map.containsKey(c) || map.get(c) < 1) {
               return false;
           }
           map.put(c, map.get(c) - 1);
       }

       return true;
    }
}