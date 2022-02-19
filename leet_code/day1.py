class MyHashMap:
    def __init__(self):
        self.num_bucket = 1000
        self.buckets = [-1] * self.num_bucket

    def put(self,key,value):
        ind = key%1000
        if self.buckets[ind] == -1:
            self.buckets[ind] = [[key,value]]
            return
        for index,kv in enumerate(self.buckets[ind]):
            if kv[0] == key:
                self.buckets[ind][index][1] = value
                return
        self.buckets[ind].append([key,value])
        return
    
    def get(self,key):
        ind = key%self.num_bucket
        if self.buckets[ind] == -1:
            return -1
        for k,v in self.buckets[ind]:
            if k ==key:
                return v
        return -1

    def remove(self,key):
        ind = key%self.num_bucket
        ind_to_remove = -1
        if self.buckets[ind] == -1:
            return
        for i, kv in enumerate(self.buckets[ind]):
            if kv[0]==key:
                ind_to_remove = i
                break
        if ind_to_remove == -1:
            return
        else:
            del self.buckets[ind][ind_to_remove]


