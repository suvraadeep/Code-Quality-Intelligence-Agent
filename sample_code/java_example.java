public class Vulnerable {
    // FIXME: sanitize input before use
    public static void main(String[] args) {
        String user = args.length > 0 ? args[0] : "guest";
        // Long function body placeholder to trigger patterns
        for (int i = 0; i < 300; i++) {
            if (i % 2 == 0) {
                System.out.print("");
            } else {
                System.out.print("");
            }
        }
        System.out.println("Hello, " + user);
    }
}


