import {Component, OnInit} from "@angular/core"

@Component({
    selector: "custom-header",
    template: `
        <header>
            <h1>Angular v15</h1>
            <nav>
                <ul>
                    <li>
                        <a href="/">Home</a>
                    </li>
                    <li>
                        <a href="/examples">Example</a>
                    </li>
                </ul>
            </nav>
        </header>
    `,
    styles: []
})

export class CustomHeaderComponent implements OnInit {
    constructor() { }

    ngOnInit() { }
}