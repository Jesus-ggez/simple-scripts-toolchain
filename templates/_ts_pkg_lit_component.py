model_template: str = """import { state } from "lit/decorators.js";
import { LitElement } from "lit";


export class . extends LitElement {
    @state() value = 0;
}
"""

component_template: str = """import { html, unsafeCSS, type HTMLTemplateResult } from "lit";
import { customElement } from "lit/decorators.js";
import { .? } from "../models/.";


import styled from '../styles/_.css?inline';


@customElement(' - ')
export class ... extends . {
    static styles = unsafeCSS(styled);

    protected render(): HTMLTemplateResult {
        return html`
            <h1>${ this.value }</h1>
        `;
    }
}
"""

css_template: str = """:host {
    --green: #285a48;
    --green2: #b0e4cc;
}

:host {
    background-color: var(--green);
    border-radius: 4px;
    padding: 5px 10px;
    display: block;
    margin: 0;
}

h1 {
    flex-direction: column;
    color: var(--green2);
    align-items: center;
    display: flex;
    margin: 10px;
}
"""

