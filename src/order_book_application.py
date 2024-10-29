class Task:
    _id = 1 
    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task._id
        Task._id += 1
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.__is_finished = False
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.__is_finished else 'NOT FINISHED'}"
        
    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True 
        

class OrderBook:
    def __init__(self):
        self.__orders = []
        self.__programmers = set()
    
    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.__orders.append(task)
        self.__programmers.add(task.programmer)
    
    def all_orders(self):
        return self.__orders  
    
    def programmers(self):
        return sorted(self.__programmers) 
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError("order not found!")
    
    def finished_orders(self) -> list:
        orders = []
        for order in self.__orders:
            if order.is_finished():
                orders.append(order)
        return orders
    
    def unfinished_orders(self) -> list:
        orders = []
        for order in self.__orders:
            if not order.is_finished():
                orders.append(order)
        return orders
    
    def status_of_programmer(self, programmer: str) -> tuple:
        status = set()
        count_fin = 0
        count_unfin = 0
        total_work_fin = 0
        total_work_unfin = 0
        for order in self.__orders:
            if order.programmer == programmer and order.is_finished():
                count_fin += 1
                total_work_fin += order.workload
            if order.programmer == programmer and not order.is_finished():
                count_unfin += 1
                total_work_unfin += order.workload
        if count_fin != 0 or count_unfin != 0:
            return (count_fin, count_unfin, total_work_fin, total_work_unfin)
        else:
            raise ValueError("programmer does not exist")


class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
        
    def help(self): 
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def add_order(self):
        try:
            description = input("description: ")
            programmer, workload = input("programmer and workload estimate: ").split(" ") 
            workload = int(workload)
        except:
            print("erroneous input")
            self.help()
            return
        self.__orderbook.add_order(description, programmer, workload)
        print("added!")
    
    def finished_orders(self):
        if len(self.__orderbook.finished_orders()) == 0:
            print("no finished tasks")
        else:
            for order in self.__orderbook.finished_orders():
                print(order)
    
    def unfinished_orders(self):
        if len(self.__orderbook.unfinished_orders()) == 0:
            print("no unfinished tasks")
        else: 
            for order in self.__orderbook.unfinished_orders():
                print(order)
    
    def mark_finished(self):
        try:
            id = int(input("id: "))
        except:
            print("erroneous input")
            self.help()
            return
        set_id = set()
        for order in self.__orderbook.all_orders():
            set_id.add(order.id)
        if not id in set_id:
            print("erroneous input")
            self.help()
            return
        self.__orderbook.mark_finished(id)
        print("marked as finished")
    
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
    
    def status_of_programmer(self):
        programmer = input("programmer: ")
        if not programmer in self.__orderbook.programmers():
            print("erroneous input")
            self.help()
            return
        result_set = self.__orderbook.status_of_programmer(programmer)
        if not result_set is None:
            print(f"tasks: finished {result_set[0]} not finished {result_set[1]}, hours: done {result_set[2]} scheduled {result_set[3]}")
        else:
            print("erroneous input")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_orders()
            elif command == "3":
                self.unfinished_orders()
            elif command == "4":
                self.mark_finished()
            elif command =="5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()



application = OrderBookApplication()
application.execute()