class Task:
    """
    Lightweight task object stored in the heap.

    Attributes:
        userId (int): Identifier of the user owning the task.
        taskId (int): Unique identifier for the task.
        priority (int): Priority of the task (larger value = higher priority).
        stale (bool): True if this heap entry has been superseded/removed.

    Ordering (__lt__):
    - Python's heapq is a *min-heap*. We implement __lt__ so that the task that
      should be executed first is considered "smaller" by heapq.
    - The comparison implemented here gives precedence to:
        1) Higher `priority` (a task with larger priority should come first).
        2) If priorities are equal, the task with the **larger** `taskId` wins.
           (i.e., ties break in favor of the larger taskId).
    """

    def __init__(self, userId: int, taskId: int, priority: int) -> None:
        self.userId = userId
        self.taskId = taskId
        self.priority = priority
        self.stale = False

    def __lt__(self, other: "Task") -> bool:
        # Return True when self should appear earlier in heapq ordering.
        if self.priority == other.priority:
            return self.taskId > other.taskId
        return self.priority > other.priority


class TaskManager:
    """
    Task manager using a heap with lazy deletion.

    Data structures:
    - self.tasks: a heap (list) storing Task objects. Heap ordering is provided
      by Task.__lt__.
    - self.id_to_task: maps taskId -> latest Task object for that id. When a task
      is edited/removed the old Task object is marked stale; new entries are pushed
      onto the heap (lazy deletion).

    Notes on behavior:
    - add(...) always inserts a new Task and updates id_to_task.
    - edit(...) marks the existing Task as stale and inserts a new Task with the
      updated priority.
    - rmv(...) marks the Task as stale (it remains in the heap until popped).
    - execTop() pops from the heap until a non-stale Task is found and returns
      its userId (or -1 if none remain).

    Time / Space complexity (n = current number of heap entries):
      - __init__(tasks): O(k log k) where k = len(tasks) (each initial add is a heap push)
        Space: O(n) for heap + mapping
      - add: O(log n) time, O(1) extra space
      - edit: O(log n) time (lazy deletion + push), O(1) extra space
      - rmv: O(1) time (mark stale), O(1) extra space
      - execTop: amortized O(log n) time (may pop multiple stale entries), O(1) extra space
    """

    def __init__(self, tasks: List[List[int]]):
        """
        Initialize TaskManager with an iterable of tasks, each represented as
        [userId, taskId, priority].

        Complexity: O(k log k) for k initial tasks (each add is O(log n)).
        """
        self.tasks: List[Task] = []
        self.id_to_task: Dict[int, Task] = {}

        for uid, tid, prio in tasks:
            self.add(uid, tid, prio)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Add a new task.

        Complexity:
            Time:  O(log n) to push onto heap
            Space: O(1) extra (heap grows by one element)
        """
        t = Task(userId, taskId, priority)
        heapq.heappush(self.tasks, t)
        self.id_to_task[taskId] = t

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Edit an existing task's priority.

        Implementation detail:
        - Mark the currently stored Task object as stale (so it will be skipped
          when popped).
        - Push a fresh Task object with the updated priority to the heap and
          update the mapping.

        Complexity:
            Time:  O(log n) (push)
            Space: O(1) extra
        """
        t = self.id_to_task[taskId]
        t.stale = True
        self.add(t.userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        """
        Remove a task by marking it stale. The actual heap entry is lazily deleted
        when popped during execTop().

        Complexity:
            Time:  O(1)
            Space: O(1)
        """
        t = self.id_to_task[taskId]
        t.stale = True

    def execTop(self) -> int:
        """
        Execute and return the userId of the highest-priority non-stale task.

        Pops from the heap until a non-stale Task is found. If no valid tasks
        remain, returns -1.

        Complexity:
            Amortized Time: O(log n) — each stale entry is popped at most once.
            Worst-case single call may pop many stale entries.
            Space: O(1) extra
        """
        while self.tasks:
            task = heapq.heappop(self.tasks)
            if not task.stale:
                return task.userId
        return -1