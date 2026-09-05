import json
import csv
import os
from datetime import datetime
import math
import random

#simple calculator

class Caculations:
    
    def check_number_validity(self, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
            return num1, num2
        except ValueError:
            print("Please enter valid numbers!")
            return None, None
            
    def add(self, num1, num2):
        result = self.check_number_validity(num1, num2)
        if result[0] is not None:
            return result[0] + result[1]
        return None
        
    def minus(self, num1, num2):
        result = self.check_number_validity(num1, num2)
        if result[0] is not None:
            return result[0] - result[1]
        return None
        
    def multiply(self, num1, num2):
        result = self.check_number_validity(num1, num2)
        if result[0] is not None:
            return result[0] * result[1]
        return None
    
    def divide(self, num1, num2):
        result = self.check_number_validity(num1, num2)
        if result[0] is not None:
            if result[1] == 0:
                print("Cannot divide by zero!")
                return None
            return result[0] / result[1]
        return None
        
    def power(self, num1, num2):
        result = self.check_number_validity(num1, num2)
        if result[0] is not None:
            return result[0] ** result[1]
        return None

# advanced calculator
class AdvancedCalculation:
    
    calculator = Calculations()
    
    def check_numbers(self, number):
        try:
            return float(number)
        except ValueError:
            print("Please enter a valid number!")
            return None
    
    def sin(self, num):
        n = self.check_numbers(num)
        if n is not None:
            return math.sin(math.radians(n))
        return None
        
    def cos(self, num):
        n = self.check_numbers(num)
        if n is not None:
            return math.cos(math.radians(n))
        return None
    
    def tan(self, num):
        n = self.check_numbers(num)
        if n is not None:
            return math.tan(math.radians(n))
        return None
        
    def cot(self, num):
        n = self.check_numbers(num)
        if n is not None and n != 0:
            return 1 / math.tan(math.radians(n))
        print("Cotangent is undefined for this angle!")
        return None
        
    def log(self, num):
        n = self.check_numbers(num)
        if n is not None and n > 0:
            return math.log(n)
        print("Log requires positive number!")
        return None
        
    def factorial(self, num):
        n = self.check_numbers(num)
        if n is not None and n >= 0 and n == int(n):
            return math.factorial(int(n))
        print("Factorial requires non-negative integer!")
        return None
    
    def bmi(self, weight, height):
        w = self.check_numbers(weight)
        h = self.check_numbers(height)
        if w is not None and h is not None and h > 0:
            return w / (h ** 2)
        print("Invalid weight or height!")
        return None

# History manager (csv)


class SimpleHistoryManager:
    def __init__(self, file_name="history.csv"):
        self.file_name = file_name
        self.history = []
        self.load()
        
    def load(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["History","answer", "Date"])
            return
            
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                return
            for row in reader:
                self.history.append({
                    "History": row[0],
                    "answer" : row[1],
                    "Date": row[2]
                })
                
    def save(self):
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["History","answer", "Date"])
            for h in self.history:
                writer.writerow([
                    h.get("History"),
                    h.get("answer"),
                    h.get("Date")
                ])
                
    def add(self, History, answer, Date=None):
        if Date is None:
            Date = datetime.now().strftime("%Y-%m-%d %H:%M")
        add_history = {
            "History": History,
            "answer" :answer,
            "Date": Date
        }
        self.history.append(add_history)
        self.save()

# advanced history manager (csv)

class AdvancedHistoryManager:
    def __init__(self, file_name="advanced_history.csv"):
        self.file_name = file_name
        self.history = []
        self.load()
        
    def load(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["question_type","your_input","answer", "Date"])
            return
            
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                return
            for row in reader:
                self.history.append({
                    "question_type": row[0],
                    "your_input" : row[1],
                    "answer" : row[2],
                    "Date": row[3]
                })
                
    def save(self):
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["question_type","your_input", "answer", "Date"])
            for h in self.history:
                writer.writerow([
                    h.get("question_type"),
                    h.get("your_input"),
                    h.get("answer"),
                    h.get("Date")
                ])
                
    def add(self, question_type, your_input, answer, Date=None):
        if Date is None:
            Date = datetime.now().strftime("%Y-%m-%d %H:%M")
        add_history = {
            "question_type": question_type,
            "your_input" : your_input,
            "answer" :answer,
            "Date": Date
        }
        self.history.append(add_history)
        self.save()


# calculator

class Calculate:
    calculation = Calculations()
    advanced_calculation = AdvancedCalculation()
    history_manager = SimpleHistoryManager()
    advanced_history_manager = AdvancedHistoryManager()
    
    def choose(self):
        print("="*60)
        print("Calculator")
        print("="*60)
        
        while True:
            print("\n1 : Simple calculator (add, minus, multiply, devide, power)")
            print("2: Advanced calculator (sin, cos, tan, cot, log, factorial, bmi)")
     
            first_choice = input("Which one? Simple calculator or Advanced calculator? Enter 1 or 2: ")
            
            if first_choice == "1":
                self.simple_calculator()
            elif first_choice == "2":
                self.advanced_calculator()
            else:
                print("Please enter a valid number (1 or 2)!")
                continue

    def simple_calculator(self):
        operations = {
            "1": {"name": "add", "func": self.calculation.add, "operator" : "+" },
            "2": {"name": "minus", "func": self.calculation.minus, "operator" : "-"},
            "3": {"name": "multiply", "func": self.calculation.multiply, "operator" : "*"},
            "4": {"name": "divide", "func": self.calculation.divide, "operator" : "/"},
            "5": {"name": "power", "func": self.calculation.power, "operator" : "**"}
        }

        operator = [ "+", "-", "*", "/", "**"]

        print("\n1: add")
        print("2: minus")
        print("3: multiply")
        print("4: divide")
        print("5: power")
        
        second_choice = input("choose: ")
        
        num1 = input("Enter first number: ").strip()
        num2 = input("Enter second number: ").strip()
        
        if second_choice in operations:
            result = operations[second_choice]["func"](num1, num2)
            calculation = ""
            for i in operator:
               if i == operations[second_choice]["operator"]:
                  calculation = f"{num1} {i} {num2}"
                  print(f"{num1} {i} {num2}")
               
            print("The result is:")
            if result is not None:
                print(result)
                self.history_manager.add(calculation , result)
        else:
            print("Invalid choice!")

    def advanced_calculator(self):
        operations = {
            "1": {
                "name": "sin",
                "func": self.advanced_calculation.sin,
                "input_count": 1
            },
            "2": {
                "name": "cos",
                "func": self.advanced_calculation.cos,
                "input_count": 1
            },
            "3": {
                "name": "tan",
                "func": self.advanced_calculation.tan,
                "input_count": 1
            },
            "4": {
                "name": "cot",
                "func": self.advanced_calculation.cot,
                "input_count": 1
            },
            "5": {
                "name": "log",
                "func": self.advanced_calculation.log,
                "input_count": 1
            },
            "6": {
                "name": "factorial",
                "func": self.advanced_calculation.factorial,
                "input_count": 1
            },
            "7": {
                "name": "BMI",
                "func": self.advanced_calculation.bmi,
                "input_count": 2
            }
        }
        
        print("\n1: sin")
        print("2: cos")
        print("3: tan")
        print("4: cot")
        print("5: log")
        print("6: factorial")
        print("7: BMI")
        
        third_choice = input("choose: ")
        
        if third_choice in operations:
            op = operations[third_choice]
            input_count = op["input_count"]
            
            if input_count == 1:
                num1 = input("Enter number: ").strip()
                result = op["func"](num1)
                self.advanced_history_manager.add(operations[third_choice]["name"], num1, result)
            else:
                weight = input("Enter weight (kg): ").strip()
                height = input("Enter height (m): ").strip()
                result = op["func"](weight, height)
                self.advanced_history_manager.add(operations[third_choice]["name"], f"Weight: {weight}, Height: {height}", result)
            
            print("The result is:")
            if result is not None:
                if third_choice == "7":
                    print(f"{result:.2f}")
                else:
                    print(result)
        else:
            print("Invalid choice!")


# Game score manager (CSV)


class GameScoreManager:
    def __init__(self, file_name="score.csv"):
        self.file_name = file_name
        self.results = []
        self.load()
        
    def load(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "calculation",
                    "correct_answer",
                    "your_answer",
                    "last_score"
                ])
            return
            
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                return
            
            for row in reader:
                try:
                    self.results.append({
                        "calculation": row[0],
                        "correct_answer": row[1],
                        "your_answer": row[2],
                        "last_score": row[3]
                    })
                except:
                    continue
                    
    def save(self):
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
            "calculation",
            "correct_answer", 
            "your_answer",
            "last_score"
           ])
            
            for r in self.results:
                writer.writerow([
                    r.get("calculation"),
                    r.get("correct_answer"),
                    r.get("your_answer"),
                    r.get("last_score")
                ])
                
    def add(self, calculation, correct_answer, your_answer, last_score):
        result = {
            "calculation": calculation,
            "correct_answer": correct_answer,
            "your_answer": your_answer,
            "last_score": last_score
        }
        
        self.results.append(result)
        self.save()


# Json manager(JSON)


class GameJsonManager:
    
    def __init__(self, file_name="score.json"):
        self.file_name = file_name
        
        self.settings = {
            "level": "easy",
            "last_score": 5,
            "win_threshold": 60
        }
        
        self.load()
        self.save()
        
    def load(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.settings = json.load(file)
                    
            except:
                self.settings = {
                    "level": "easy",
                    "last_score": 5,
                    "win_threshold": 60
                }
                    
    def save(self):
        with open(self.file_name, "w") as file:
            json.dump(self.settings, file, indent=2)
            
    def set_level_score(self, level, score):
        self.settings["level"] = level
        self.settings["last_score"] = score
        self.save()
        return True
        
    def get_level(self):
        return self.settings.get("level", "easy")
    
    def get_last_score(self):
        return self.settings.get("last_score", 5)
    
    def get_win_threshold(self):
        return self.settings.get("win_threshold", 60)
    
    def set_win_threshold(self, threshold):
        self.settings["win_threshold"] = threshold
        self.save()


# main game (Game)

class Game:
    score_manager = GameScoreManager()
    json_manager = GameJsonManager()
    
    def __init__(self):
        self.last_score = self.json_manager.get_last_score()
        self.current_score = self.last_score        
        self.base_level = self.json_manager.get_level()
        self.win_threshold = self.json_manager.get_win_threshold()
        self.lose_game = self.last_score - 30
        
        self.easy = 0
        self.medium = 0
        self.hard = 0
        self.game_over = False
        
        self.levels = {
            "easy": {
                "count": 0,
                "max": 5,
                "points": 3,
                "penalty": 2
            },
            "medium": {
                "count": 0,
                "max": 5,
                "points": 5,
                "penalty": 4
            },
            "hard": {
                "count": 0,
                "max": 5,
                "points": 7,
                "penalty": 6
            }
        }
           
    def generate_question(self, level):
        if level == "easy":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            op = random.choice(["+", "-"])
            
        elif level == "medium":
            op = random.choice(["+", "-", "*"])
            if op == "*":
                a = random.randint(5, 15)
                b = random.randint(5, 15)
            else:
                a = random.randint(100, 200)
                b = random.randint(100, 200)
            
        else:  # hard
            op = random.choice(["+", "-", "*", "/"])
            if op == "*" or op == "/":
                a = random.randint(5, 20)
                b = random.randint(5, 20)
            else:
                a = random.randint(100, 300)
                b = random.randint(100, 300)
        
        question = f"{a} {op} {b}"
        
        if op == "+":
            answer = a + b
            
        elif op == "-":
            answer = a - b
            
        elif op == "*":
            answer = a * b
            
        else:
            answer = round(a / b, 2)
        
        return question, answer
    
    def play_round(self, level):
        print("\nEnter 'exit' to quit the game at any time.")
        
        question, correct_answer = self.generate_question(level)
        
        print(f"\n{question} = ?")

        while True:
            user_input = input("Your answer (or 'exit'): ").strip().lower()
            
            # exit game
            if user_input == "exit" or user_input == "quit":
                print(
                    "\nYou exited the game. "
                    "Current session score lost!"
                )
                
                self.current_score = 0
                self.game_over = True
                return
            
            try:
                your_answer = float(user_input)
                break
                
            except ValueError:
                print("Please enter a valid number or 'exit'!")
                
        level_data = self.levels[level]
        
        if your_answer == correct_answer:
            level_data["count"] += 1
            self.current_score += level_data["points"]
            
            print(f"Correct! +{level_data['points']} points")
            
        else:
            self.current_score -= level_data["penalty"]            
            print(f"Wrong! -{level_data['penalty']} points")            
            print(f"Correct answer was: {correct_answer}")
        
        # save CSV
        self.score_manager.add(
            question,
            correct_answer,
            your_answer,
            self.current_score
        )
        
        print(f"Current score: {self.current_score}")
        self.win_or_lose_game()


    def win_or_lose_game(self):
        if self.current_score >= self.win_threshold:
            
            print(
                f"\n You reached "
                f"{self.win_threshold} points! You win!"
            )
            
            self.game_over = True
            
        elif self.current_score <= self.lose_game:
            
            print(
                f"\n Your score reached "
                f"{self.lose_game} points! You lose!"
            )
            
            self.game_over = True


    def play_game(self):
        self.last_score = self.json_manager.get_last_score()
        self.win_threshold = self.json_manager.get_win_threshold()
        self.lose_game = self.last_score - 30
        self.current_score = self.last_score
        
        print("\n" + "=" * 50)
        print(" MATH GAME STARTED")
        print("=" * 50)
        
        print(f"Starting score: {self.current_score}")
        print(f"Win Threshold: {self.win_threshold}")
        print(f"Lose Threshold: {self.lose_game}")
        print("Answer 5 questions in each level to progress!")
        print(
            " Enter 'exit' at any time to quit "
            "(score will be lost)"
        )
        
        for level in ["easy", "medium", "hard"]:
            
            if self.game_over:
                break
            
            print(f"\nLevel: {level.upper()}")
            print("-" * 30)
            
            while (
                self.levels[level]["count"] < 5
                and not self.game_over
            ):
                
                self.play_round(level)
                
                if self.current_score <= self.lose_game:
                    self.game_over = True
                    break

# بررسی نتیجه نهایی بازی
        
        # if win:
        if self.current_score >= self.win_threshold:
            
            print(
                "\nCONGRATULATIONS! "
                "YOU WON THE GAME!"
            )
            
            print(f"🏆 Final score: {self.current_score}")
            
            self.last_score = self.current_score
            new_threshold = self.last_score + 60            
            self.json_manager.set_win_threshold(new_threshold)
            
            print(f"Next win threshold: {new_threshold}")
            
        #if lose:
        elif self.current_score <= self.lose_game:
            
            print(
                "\nGAME OVER! "
                "BETTER LUCK NEXT TIME!"
            )
            self.current_score = 0
        elif self.game_over:
            
            print("\nYou exited the game.")
        self.json_manager.set_level_score(
            self.base_level,
            self.last_score
        )

# بخش ۸: برنامه اصلی (Main)


def main():
    calculator = Calculate()
    
    while True:
        print("="*60)
        print("Program Starts")
        print("="*60)
    
        print("1 : Calculator")
        print("2 : Math Game")
        print("3 : Exit")
        
        choose = input(
            "Please choose (by number) :"
        )
    
        if choose == "1":
            calculator.choose()
            
        elif choose == "2":
            game = Game()
            game.play_game()
            
        elif choose == "3":
            print("Goodbye...")
            break
            
        else:
            print("Please enter valid number")
            continue
            
if __name__ == "__main__":
    main()
