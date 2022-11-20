class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_string = ""
        for s in strs:
            encode_string += '\t' + s
        
        print(encode_string)
        return encode_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        #decode_string = s.replace('\t',' ')
        decode_lst = []
        for s in s.split("\t"):
            decode_lst.append(s)
        
        return decode_lst[1:]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))