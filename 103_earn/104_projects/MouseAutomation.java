import java.awt.Robot;

public class MouseAutomation {
    public static void main(String... args) throws Exception {
        Robot robot = new Robot();
        while (true) {
            robot.mouseMove(400, 400);
            Thread.sleep(3000);
        }
    }
}