class MyList(list):
    def sum(self):
        return sum(self)
    
    def append(self, item):
        print("a new item has been appended!")
        super().append(item)

nums = MyList([1, 2, 3])
print(nums.sum())  # 6

nums.append(2)
