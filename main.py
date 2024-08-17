# домашнее задание OD01

# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения задачи
        self.completed = False  # Статус задачи (по умолчанию не выполнено)
        self.tasks = []  # Список для хранения всех задач

    def add_task(self, description, deadline):
        """
        Функция для добавления новой задачи.
        """
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f'Задача "{description}" добавлена со сроком выполнения до {deadline}')

    def mark_completed(self, description):
        """
        Функция для отметки задачи как выполненной.
        """
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                print(f'Задача "{description}" отмечена как выполненная')
                return
        print(f'Задача "{description}" не найдена')

    def show_uncompleted_tasks(self):
        """
        Функция для вывода списка текущих (не выполненных) задач.
        """
        print("Текущие (не выполненные) задачи:")
        for task in self.tasks:
            if not task.completed:
                print(f"- {task.description} (Срок: {task.deadline})")
        print("\n")

    def show_completed_tasks(self):
        """
        Функция для вывода списка выполненных задач.
        """
        print("Выполненные задачи:")
        for task in self.tasks:
            if task.completed:
                print(f"- {task.description} выполнена, срок: {task.deadline})")
        print("\n")

    def __str__(self):
        """
        Строковое представление задачи.
        """
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


# Пример использования класса
task_manager = Task("Example", "2024-08-15")  # Это просто для создания экземпляра

# Добавление задач
task_manager.add_task("Купить продукты", "2024-08-20")
task_manager.add_task("Сдать отчет", "2024-08-19")

# Отметить задачу как выполненную
task_manager.mark_completed("Купить продукты")

# Вывод текущих (не выполненных) задач
task_manager.show_uncompleted_tasks()
