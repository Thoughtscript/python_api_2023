import { Component, OnInit } from "@angular/core"
import { ExampleService } from '../../services/example.service'

@Component({
    selector: "example",
    template: `
    <main>
        <div id="flex-wrapper">
        <table>
            <tr>
                <th>Example {{ '{' }} UUID - Name {{ '}' }}</th>
            </tr>
            <tr *ngFor="let example of examples">
                <td>{{example}}</td>
            </tr>
        </table>
        </div>
    </main>
  `,
    styles: []
})

export class ExampleComponent implements OnInit {
    //Make array to hold data
    public examples: string[] = [];

    //Inject the relevant service here
    constructor(private _exampleService: ExampleService) {  }

    ngOnInit() { this.getExamples(); }
    
    getExamples() {
        // Casting response Objects
        this._exampleService.getEvents().subscribe((res: Object) => {
            const E_R = res as string[]
            const SLICED_EVENTS = E_R.slice(0, 5);
            this.examples = SLICED_EVENTS;
            console.log(this.examples);
        });
    }
}