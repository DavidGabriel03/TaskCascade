from Task import TodoList, Task

todo = TodoList()
todo.load_from_json()

def afiseaza_taskuri():
    print("\n--- Lista taskuri ---")
    for task in todo.get_tasks():
        print(f"[{task.id}] {task}")

while True:
    print("\nMeniu principal:")
    print("1 - Adaugă task")
    print("2 - Afișează toate taskurile")
    print("3 - Șterge task")
    print("4 - Editează task")
    print("5 - Ieșire")
    opt = input("Alege opțiunea: ")

    if opt == "1":
        id = int(input("ID: "))
        name = input("Nume: ")
        description = input("Descriere: ")
        status = input("Status (True/False): ") == "True"
        start_time = input("Start time: ")
        end_time = input("End time: ")
        task = Task(id, name, description, status, start_time, end_time)
        todo.add_task(task)
        todo.save_to_json()
        print("✔ Task adăugat.")

    elif opt == "2":
        afiseaza_taskuri()

    elif opt == "3":
        afiseaza_taskuri()
        id = int(input("ID-ul taskului de șters: "))
        task = todo.get_task_by_id(id)
        if task:
            todo.remove_task(task)
            todo.save_to_json()
            print("✔ Task șters.")
        else:
            print("❌ Taskul nu a fost găsit.")

    elif opt == "4":
        afiseaza_taskuri()
        id = int(input("ID-ul taskului de editat: "))
        task = todo.get_task_by_id(id)
        if not task:
            print("❌ Taskul nu a fost găsit.")
            continue

        print("Ce dorești să editezi?")
        print("1 - Nume")
        print("2 - Descriere")
        print("3 - Status")
        print("4 - Ora de început")
        print("5 - Ora de sfârșit")
        edit_opt = input("Alege opțiunea: ")

        index = todo.tasks.index(task)

        if edit_opt == "1":
            name = input("Noul nume: ")
            todo.editTaskbyName(index, name)
        elif edit_opt == "2":
            desc = input("Noua descriere: ")
            todo.editTaskbyDescription(index, desc)
        elif edit_opt == "3":
            status = input("Noul status (True/False): ") == "True"
            todo.editTaskbyStatus(index, status)
        elif edit_opt == "4":
            start = input("Nou start time: ")
            todo.editTaskbyStartTime(index, start)
        elif edit_opt == "5":
            end = input("Nou end time: ")
            todo.editTaskbyEndTime(index, end)
        else:
            print("❌ Opțiune invalidă.")
            continue

        todo.save_to_json()
        print("✔ Task modificat.")

    elif opt == "5":
        print("👋 Ieșire din aplicație.")
        break

    else:
        print("❌ Opțiune invalidă.")