class Solution {
    public boolean wordPattern(String pattern, String s) {
        
        String[] word = s.split(" ");

        // If pattern and s do not have same size
        if (pattern.length() != word.length) {
            return false;
        }

        HashMap<Character, String> map = new HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
        

        if (map.containsKey(c)) {
            if(!map.get(c).equals(word[i])){
                    return false;
                }
        } else {
            if(map.containsValue(word[i])){
                    return false;
                }
        }
        map.put(c, word[i]);
        }
        
        return true;

    }

}