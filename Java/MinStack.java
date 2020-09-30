class MinStack {
    
    Stack<Integer> stack=new Stack<>();
    Stack<Integer> minstack=new Stack<>();
    
    /** initialize your data structure here. */
    public MinStack() {
        this.stack = stack;
        this.minstack = minstack;
        //this.min=min;
    }
    
    public void push(int x) {
        if(minstack.isEmpty() || x<=minstack.peek())
            minstack.push(x);
        stack.push(x);
    }
    
    public void pop() {
       if(stack.peek().equals(minstack.peek())) 
            minstack.pop();
        stack.pop();
        
    }
    
    public int top() {
        
        return stack.peek();
    }
    
    public int getMin() {
        
        return minstack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */