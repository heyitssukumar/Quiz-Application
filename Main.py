import json
def quiz_App():
    print("\033[1;32;40m")  # Set text color to green]")
    print(f"{'=' * 50}")
    print(f"{' ' * 15}QUIZ APP{' ' * 15}")
    print(f"{'=' * 50}")
    print("Welcome to the Quiz App!")
    try:
      with open('question.json', 'r') as file:
            questions = json.load(file)
    except FileNotFoundError:
        print("Error: question.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from question.json.")
        return
    count = 0
    a = 0
    for options in questions.values():
        for ch in options:
            a += 1
            print("\033[1;34;40m")  # Set text color to blue]")
            print("Q",a,": ",ch['question'], end="\n")
            for i, option in enumerate(ch['options'], start=1):
                print(f"{i}. {option}")
            print("\033[1;32;40m")  # Set text color to green
            print(f"{'-'*50}\n")
            while True:
                try:
                    print("\033[1;33;40m")  # Set text color to yellow
                    answer = int(input("Enter the number of your answer: "))
                    print("\033[1;32;40m")  # Set text color to green
                    print(f"{'-'*50}\n")
                except ValueError:
                    print("\033[31;40m")  # Set text color to red
                    print("Invalid input. Please enter a number.")
                    print("\033[1;32;40m")  # Set text color to green
                    print(f"{'-'*50}\n")
                    continue
                if answer >= 1 and answer <= len(ch['options']):
                    if answer == ch['answer']:
                        print("\033[1;32;40m")  # Set text color to green]")
                        print("Correct!\n")
                        print(f"{'-'*50}\n")
                        count += 1
                        break
                    else:
                        print("\033[31m")
                        print(f"Wrong! The correct answer is: {ch['options'][ch['answer'] - 1]}\n")
                        print("\033[32;40m")
                        print(f"{'-'*50}\n")
                        break
                else:
                    print("\033[31;40m")  # Set text color to red
                    print(f"Invalid option. Please enter a number between 1 and {len(ch['options'])}.")
                    continue
    length =0        
    for options in questions.values():
        for ch in options:
            length += 1           
    print(f"Your total score is: {count}/{length}\n")

quiz_App()