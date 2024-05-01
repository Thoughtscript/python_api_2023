import {Injectable} from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Injectable()
export class ExampleService {
    constructor(private http: HttpClient) {  }
    
    getEvents() { return this.http.get('http://localhost:5001/api/db/examples'); }
}
