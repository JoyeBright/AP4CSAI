class MyList(list):
    def sum(self):
        return sum(self)

nums = MyList([1, 2, 3])
print(nums.sum())  # 6
