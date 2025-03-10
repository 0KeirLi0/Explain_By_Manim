from manim import *
import numpy as np

class LLNScene(Scene):
    def construct(self):
        # Title
        title = Text("Law of Large Numbers").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Set up axes for the running average plot
        axes = Axes(
            x_range=[0, 1000, 100],  # Up to 1000 flips
            y_range=[0, 1, 0.25],    # Average between 0 and 1
            axis_config={"color": BLUE},
            tips=False,
        ).scale(0.7).to_edge(DOWN, buff=0.5)
        axes_labels = axes.get_axis_labels(x_label="Number of Flips", y_label="Running Average")
        self.play(Create(axes), Write(axes_labels))
        
        # Expected value line at 0.5
        expected_line = axes.get_horizontal_line(axes.c2p(1000, 0.5), color=YELLOW)
        expected_label = Text("Expected Value = 0.5").scale(0.5).next_to(expected_line, RIGHT)
        self.play(Create(expected_line), Write(expected_label))
        self.wait(1)

        # Function to simulate coin flips and compute running average
        def simulate_flips(n):
            flips = np.random.randint(0, 2, n)  # 0 for tails, 1 for heads
            return np.cumsum(flips) / np.arange(1, n + 1)  # Running average

        # Stages: 1, 10, 100, 1000 flips
        stages = [1, 10, 100, 1000]
        for n in stages:
            # Simulate flips
            averages = simulate_flips(n)
            
            # Plot the running average
            plot = axes.plot_line_graph(
                x_values=np.arange(1, n + 1),
                y_values=averages,
                line_color=GREEN,
                add_vertex_dots=False,
            )
            
            # Text to show current stage
            stage_text = Text(f"{n} Flips: Avg ≈ {averages[-1]:.3f}").scale(0.8).move_to(UP * 2)
            
            # Coins animation (simple representation)
            coins = VGroup(*[Dot(radius=0.1) for _ in range(min(n, 10))])  # Limit to 10 visible coins
            coins.arrange(RIGHT, buff=0.2).move_to(UP * 1.5)
            if n > 10:
                extra_text = Text(f"+ {n-10} more...").scale(0.5).next_to(coins, RIGHT)
                coins.add(extra_text)

            # Animate
            self.play(Write(coins), Write(stage_text))
            self.play(Create(plot))
            self.wait(2)
            
            # Clean up
            self.play(FadeOut(coins), FadeOut(plot), FadeOut(stage_text))

        # Final message
        final_text = Tex(r"As $n \to \infty$, the average $\to$ 0.5").scale(1).move_to(UP * 2)
        self.play(Write(final_text))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(Group(*self.mobjects)))

# Add the main entry point
if __name__ == "__main__":
    import sys
    from manim.utils.module_ops import get_scene_classes_from_module
    
    # Get all scene classes defined in this module
    scenes = get_scene_classes_from_module(sys.modules[__name__])
    
    # If you want to render a specific scene, you can do:
    # python your_file.py LLNScene
    if len(sys.argv) > 1:
        scene_name = sys.argv[1]
        if scene_name in scenes:
            scene = scenes[scene_name]()
            scene.render()
    else:
        # Default to rendering the LLNScene
        LLNScene().render()