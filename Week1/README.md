Week1 学习笔记
# 1. 用add first或add last这套新的API改写Deque的代码

```
        Deque<String> deque = new LinkedList<String>();
        deque.addFirst("a");
        deque.addFirst("b");
        deque.addFirst("c");
        System.out.println(deque);

        String str = deque.peekFirst();
        System.out.println(str);
        System.out.println(deque);

        while (deque.size() > 0) {
            System.out.println(deque.removeFirst());
        }
        System.out.println(deque);
```

# 2. 分析Queue和Priority Queue的源码
## 2.1 Queue 源码分析
1. 继承自Collection<E>接口，本身也只是个接口。
2. 队列的常见方法有
    - boolean add(E e);
    - boolean offer(E e);
    - E remove();
    - E poll();
    - E element();
    - E peek();
3. 实现类
    - ArrayBlockingQueue<E>
    - ConcurrentLinkedQueue<E>
    - PriorityBlockingQueue<E>
    - DelayQueue<E,extends,Delayed>
    - LinkedBlockingQueue<E>
    - SynchronousQueue<E>
## 2.2 Priority Queue 源码分析
1. 实现类，继承自AbstractQueue<E>
2. 实现类多个接口：
    - BlockingQueue<E>
    - Collection<E>
    - Iterable<E> 
    - Queue<E> （重点）
3. 核心方法
- add(E e)
- put(E e)
- clear()
- offer(E e)
- peek()
- poll()
- remove(Object o)
- toArray()
4. 特点
- 不允许null元素
- Comparable 实现自定义排序
- toArray 可以返回当前的数组（无序）
- iterator() 可以迭代该队列

# 本周内容总结脑图
week1内容其实挺多，尤其是跟着课程把附带的作业和源码分析。我至少投入了10个小时，才完成了大部分的任务。
至于学到了啥，我觉得整理在自己的思维导图更合适。每次新知识，都可以对自己的知识体系进行填充补全，而不是零散的知识体系。
中等和困难题，对我难说有点做不了，后续渐渐逼自己去尝试做出来。
