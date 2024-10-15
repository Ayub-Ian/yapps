export const Table = ({ children }) => {
    return (
        <table>
            {children}
        </table>
    );
};

export const Thead = ({ children }) => {
    return (
        <thead>
            <tr>
                {children}
            </tr>
        </thead>
    );
};

export const Trow = ({ children }) => {
    return (
        <tr>
            {children}
        </tr>
    );
};

export const Tbody = ({ children }) => {
    return (
        <tbody>
            {children}
        </tbody>
    );
};

export const Tcell = ({ children }) => {
    return (
        <td>
            {children}
        </td>
    );
};