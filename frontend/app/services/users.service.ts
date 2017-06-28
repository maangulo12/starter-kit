import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class UsersService {
    
    // API: users URL
    private url: string = '/api/v1/users';

    // Constructor function
    constructor(private http: Http) {}    

    getOptions() {
        let header = new Headers({ 'Content-Type': 'application/json'});
        return new RequestOptions({ headers: header });
    }

    // Add user function (returns the added user)
    addUser(user: any) {
        let data = JSON.stringify(user);
        return this.http.post(this.url, data, this.getOptions())
            .map(res => res.json());
    }

    // Delete user (returns the deleted user)
    deleteUser(id: string) {
        return this.http.delete(this.url + '/' + id, this.getOptions())
            .map(res => res.json());
    }

    // Update user (returns the updated user)
    updateUser(user: any) {
        let data = JSON.stringify(user);
        return this.http.put(this.url + '/' + user.id, data, this.getOptions())
            .map(res => res.json());
    }

    // Get user (returns the specific user)
    getUser(id: string) {
        return this.http.get(this.url + '/' + id, this.getOptions())
            .map(res => res.json());
    }

    // Get list of users (returns the list of users)
    getUsers() {
        return this.http.get(this.url, this.getOptions())
            .map(res => res.json());
    }
    
}