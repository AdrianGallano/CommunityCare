import React from "react"
import LogInService from "@/services/LoginService";

const LogIn = () => {
    let token = LogInService();
    console.log(token);
    return (
        <>
            <button>LogIn</button>
        </>
    );
}


export default LogIn;