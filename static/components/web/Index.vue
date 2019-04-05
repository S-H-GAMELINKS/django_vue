<template>
    <div>
        <h1>Index Pages</h1>

        <p v-for="(todo, key, index) in todos" :key=index>
            {{todo.title}}: {{todo.content}}
        </p>

        <form>
            <div class="form-group">
                <label>Tittle</label>
                <input class="form-control" v-model="title" placeholder="Input your post title ......">
            </div>
            <div class="form-group">
                <label>Content</label>
                <input class="form-control" v-model="content" placeholder="Input your post title ......">
            </div>
        </form>
        <p>
            <button type="button" class="btn btn-primary" v-on:click="createTodo">Create</button>
        </p>
    </div>    
</template>

<script>
import axios from 'axios';
import $ from 'jquery'

export default {
    data: function() {
        return {
            todos: [],
            title: "",
            content: "",
        }
    },
    mounted: function() {
        this.getTodos();
    },
    methods: {
        getTodos: function() {
            axios.defaults.headers['Accept'] = 'application/json';

            axios.get('/todos/', {auth: {username: "admin", password: "123"}}).then((response) => {
                for(var i = 0; i < response.data.length; i++) {
                    this.todos.push({title: response.data[i].title_text, content: response.data[i].content_text});
                }
                console.log(this.todos);
                console.log(response);
            }, (error) => {
                alert(error);
            })
        },
        createTodo: function() {
            axios.defaults.headers['Content-Type'] = 'application/json';

            axios.post('/todos/', {title_text: this.title, content_text: this.content}).then((response) => {
                if (this.title === "" || this.content === "") {
                    alert("Can't be black in Title or Content!!");
                } else {
                    alert("Success!");
                    this.todos.push({title: this.title, content: this.content});
                    this.title = "";
                    this.content = "";
                    this.$forceUpdate();
                }
            }, (error) => {
                console.log(error);
                alert(error);
            })
        }
    }
}
</script>