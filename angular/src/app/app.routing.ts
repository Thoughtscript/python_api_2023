import { NgModule } from "@angular/core"
import { Routes, RouterModule } from "@angular/router"
import { HomeComponent } from "./modules/home/home.component"
import { ExampleComponent } from "./modules/examples/example.component"

const routes: Routes = [
    {
        path: "",
        component: HomeComponent
    },
    {
        path: "examples",
        component: ExampleComponent
    },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}