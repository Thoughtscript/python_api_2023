import { Component, OnInit } from "@angular/core"

@Component({
    selector: "custom-footer",
    template: `
    <footer>
        <a rel="noopener" href="https://leetcode.com/Thoughtscript/" target="_blank">LeetCode</a>
        <a rel="noopener" href="https://www.thoughtscript.io/" target="_blank">Thoughtscript.io</a>
        <a rel="noopener" href="https://thoughtscript-io.onrender.com/assets/pdf/Complete%20Resume%202022.pdf" target="_blank">Resume</a>
    </footer>
  `,
    styles: [ ]
})

export class CustomFooterComponent implements OnInit {
    constructor() {}
    
    ngOnInit() {}
}